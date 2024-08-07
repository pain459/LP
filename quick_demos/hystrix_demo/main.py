from external_service import ExternalService
from external_service_command import ExternalServiceCommand

def main():
    external_service = ExternalService()

    for _ in range(10):
        command = ExternalServiceCommand(external_service)
        result = command.execute()
        print("Result:", result)

if __name__ == "__main__":
    main()
