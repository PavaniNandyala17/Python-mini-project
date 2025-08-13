class ERQueue: 
    def __init__(self): 
        self. critical_queue = [] # Queue for critical patients 
        self.non_critical_queue = [] # Queue for non-critical patients 
    def enqueue (self, name, is_critical): 
        if is_critical: 
            self. critical_queue.append(name) 
        else: 
            self.non_critical_queue.append(name) 
    def dequeue(self): 
        if self. critical_queue: 
            return self.critical_queue.pop(0) 
        elif self.non_critical_queue: 
            return self.non_critical_queue.pop(0) 
        else: 
            return None 
# Create the queue system 
queue_system = ERQueue() 
# Taking input dynamically 
num_patients = int (input ("Enter the number of patients: ")) 
for i in range(num_patients): 
name = input ("Enter patient's name: ") 
is_critical = input ("Is the patient critical? (yes/no): ").strip().lower() == 
'yes' 
queue_system.enqueue(name, is_critical) 
# Processing the queue based on entry order and priority 
num_treatments = num_patients # Treat all patients in queue 
for j in range(num_treatments): 
treated_patient = queue_system.dequeue() 
if treated_patient: 
print(treated_patient) 
