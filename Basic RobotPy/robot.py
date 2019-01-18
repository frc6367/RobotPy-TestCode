import wpilib
import wpilib.drive
import ctre

from magicbot import MagicRobot
from components.FlashDrive import FlashDrive

class MyRobot(MagicRobot):

    flashdrive : FlashDrive

    def createObjects(self):
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


    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.flashdrive_drivetrain.setSafetyEnabled(True)
    
    def teleopPeriodic(self):
        self.flashdrive_drivetrain.arcadeDrive(self.joystick.getY(),self.joystick.getX(),True)

if __name__ == '__main__':
    wpilib.run(MyRobot)


