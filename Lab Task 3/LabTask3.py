class ModelBasedReflexAgent:
    def __init__(self, desired_temperature, memory_file="memory.txt"):
        self.desired_temperature = desired_temperature
        self.memory_file = memory_file
        self.current_temperature = None

        file = open(self.memory_file, "a")
        file.close()
        with open(self.memory_file, "r+") as f:
            if not f.read().strip():
                f.write("Temperature,Action\n")

    def perceive(self, current_temperature):
        self.current_temperature = current_temperature
        return current_temperature

    def load_memory(self, temp):
        with open(self.memory_file, "r") as f:
            next(f)
            for line in f:
                saved_temp, action = line.strip().split(",", 1)
                if int(saved_temp) == temp:
                    return action
        return None


    def save_memory(self, temp, action):
        with open(self.memory_file, "a") as f:
            f.write(f"{temp},{action}\n")

    def act(self, current_temperature):
        action = self.load_memory(current_temperature)
        if action:
            return f"(From Memory) {action}"

        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"

        self.save_memory(current_temperature, action)
        return f"(Calculated) {action}"


rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desired_temperature = 16
agent = ModelBasedReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")