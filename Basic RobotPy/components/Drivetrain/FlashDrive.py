import wpilib
import ctre

class FlashDrive:
    left_master: ctre.WPI_TalonSRX
    left_slave1: ctre.WPI_VictorSPX
    left_slave2 : ctre.WPI_VictorSPX
    right_master : ctre.WPI_TalonSRX
    right_slave1 : ctre.WPI_VictorSPX
    right_slave2 : ctre.WPI_VictorSPX
    left_drive : wpilib.SpeedControllerGroup
    right_drive : wpilib.SpeedControllerGroup
    drivetrain : wpilib.drive.DifferentialDrive
    
    def execute(self):
        pass

