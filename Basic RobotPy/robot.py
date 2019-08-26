import wpilib
import rev
import ctre
from magicbot import MagicRobot
from components.Drivetrain.FlashDrive import FlashDrive
from components.Elevator.Elevator import Elevator
from components.Elevator.Constants import Constants

class MyRobot(MagicRobot):

    flashdrive : FlashDrive
    elevator: Elevator
    constants : Constants

    def createObjects(self):
        self.intake_motor = rev.CANSparkMax(7,rev.MotorType.kBrushless)
        self.flashdrive_left_master = ctre.WPI_TalonSRX(1)
        self.flashdrive_left_slave1 = ctre.WPI_VictorSPX(2)
        self.flashdrive_left_slave2 = ctre.WPI_VictorSPX(3)
        self.flashdrive_right_master = ctre.WPI_TalonSRX(4)
        self.flashdrive_right_slave1 = ctre.WPI_VictorSPX(5)
        self.flashdrive_right_slave2 = ctre.WPI_VictorSPX(6)
        
        self.flashdrive_left_drive = wpilib.SpeedControllerGroup(
            self.flashdrive_left_master,
            self.flashdrive_left_slave1,
            self.flashdrive_left_slave2
        )
        self.flashdrive_right_drive = wpilib.SpeedControllerGroup(
            self.flashdrive_right_master,
            self.flashdrive_right_slave1,
            self.flashdrive_right_slave2
        )
        self.flashdrive_drivetrain = wpilib.drive.DifferentialDrive(self.flashdrive_left_drive, self.flashdrive_right_drive)
        self.joystick = wpilib.Joystick(0)
        self.elevator_motor = ctre.WPI_TalonSRX(7)

    def robotInit(self):
        # Factory default hardware to prevent unexpected behavior
        self.initElevator()

    def initElevator(self):
        # reset to factory defaults upon init
        self.elevator_motor.configFactoryDefault()
        # determine quadrature encoder on the Talon.
        self.elevator_motor.configSelectedFeedbackSensor(
            ctre.FeedbackDevice.CTRE_MagEncoder_Relative, 
            self.constants.kPIDLoopIdx, 
            self.constants.kTimeoutMs
        )
        #Invert LED responses
        self.elevator_motor.setSensorPhase(True)
        self.elevator_motor.setInverted(False)
        #Set relevant time frames to be as fast as ppssible
        self.elevator_motor.setStatusFramePeriod( 
            ctre.WPI_TalonSRX.StatusFrameEnhanced.Status_13_Base_PIDF0, 
            10, 
            self.constants.kTimeoutMs )
        self.elevator_motor.setStatusFramePeriod(
            ctre.WPI_TalonSRX.StatusFrameEnhanced.Status_10_MotionMagic,
            10,
            self.constants.kTimeoutMs )
        #Set peak and nominal inputs
        self.elevator_motor.configNominalOutputForward(0, self.constants.kTimeoutMs)
        self.elevator_motor.configNominalOutputReverse(0, self.constants.kTimeoutMs)
        self.elevator_motor.configPeakOutputForward(1, self.constants.kTimeoutMs)
        self.elevator_motor.configPeakOutputReverse(-1, self.constants.kTimeoutMs)
        self.elevator_motor.selectProfileSlot(self.constants.kSlotIdx, self.constants.kPIDLoopIdx)
        self.elevator_motor.config_kF(self.constants.kSlotIdx, self.constants.kGains.kF, self.constants.kTimeoutMs)
        self.elevator_motor.config_kP(self.constants.kSlotIdx, self.constants.kGains.kP, self.constants.kTimeoutMs)
        self.elevator_motor.config_kI(self.constants.kSlotIdx, self.constants.kGains.kI, self.constants.kTimeoutMs)
        self.elevator_motor.config_kD(self.constants.kSlotIdx, self.constants.kGains.kD, self.constants.kTimeoutMs)
        #Set acceleration and vcruise velocity
        self.elevator_motor.configMotionCruiseVelocity(15000, self.constants.kTimeoutMs)
        self.elevator_motor.configMotionAcceleration(6000, self.constants.kTimeoutMs)

		#Zero the sensor
        self.elevator_motor.setSelectedSensorPosition(0, self.constants.kPIDLoopIdx, self.constants.kTimeoutMs)



    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.flashdrive_drivetrain.setSafetyEnabled(True)
    
    def teleopPeriodic(self):
        self.flashdrive_drivetrain.arcadeDrive(self.joystick.getY(),self.joystick.getX(),True)

if __name__ == '__main__':
    wpilib.run(MyRobot)


