from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.Encoder import *


# Initialize the DC Motor with a specific serial number and channel
def init_motor(serial_number):
    motor = DCMotor()
    motor.setDeviceSerialNumber(serial_number)
    
    motor.openWaitForAttachment(5000)  # Wait for the motor to be attached
    return motor

# Initialize the Encoder with a specific serial number and channel
def init_encoder(serial_number):
    encoder = Encoder()
    encoder.setDeviceSerialNumber(serial_number)
    
    encoder.openWaitForAttachment(5000)  # Wait for the encoder to be attached
    return encoder

# Motor control function
def control_motor(motor, encoder, target_position):
    if(target_position<0):
        motor.setTargetVelocity(-0.4)  # Set motor speed (from -1.0 to 1.0)

        while True:
            current_position = encoder.getPosition()
            print(f"Encoder Position: {current_position}")

            if current_position <= target_position:
                motor.setTargetVelocity(0)  # Stop the motor when target position is reached
                print("Target position reached.")
                break
    
    else:
        motor.setTargetVelocity(0.4)  # Set motor speed (from -1.0 to 1.0)

        while True:
            current_position = encoder.getPosition()
            print(f"Encoder Position: {current_position}")

            if target_position <= current_position:
                motor.setTargetVelocity(0)  # Stop the motor when target position is reached
                print("Target position reached.")
                break
        
# Main function
def main():
    # List of serial numbers and channels for each motor/encoder pair
    motor_configs = [
        
        
        {"serial_number": 146680}
        
        
    ]

    motors = []
    encoders = []
    # Initialize all motors and encoders
    for config in motor_configs:
        motor = init_motor(config["serial_number"])
        encoder = init_encoder(config["serial_number"])
        motors.append(motor)
        encoders.append(encoder)

    try:
        target_positions = [-900]  # Example target positions for each motor for fo rward give negative tsrget position

        # Control each motor to reach its target position
        for motor, encoder, target_position in zip(motors, encoders, target_positions):
            control_motor(motor, encoder, target_position)
      
    except PhidgetException as e:
        print("Phidget Error: " + e.details)

    finally:
        # Close all motors and encoders
        for motor, encoder in zip(motors, encoders):
            motor.close()
            encoder.close()

if __name__ == "__main__":
    main()