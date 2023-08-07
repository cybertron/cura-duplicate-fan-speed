# Copy the fan speed settings from the primary fan to a second one.
# This code is provided as-is. Use at your own risk.

from ..Script import Script
class DuplicateFanSpeed(Script):
    version = "1.0"
    def __init__(self):
        super().__init__()
    
    def getSettingDataString(self):
        return """{
            "name":"Duplicate fan speed """ + self.version + """",
            "key": "DuplicateFanSpeed",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "target_fan":
                {
                    "label": "Target Fan",
                    "description": "ID of secondary fan which should be set to the same speed as the primary one.",
                    "type": "int",
                    "default_value": 2
                }
            }
        }"""
    
    def execute(self, data):
        target_fan = self.getSettingValueByKey("target_fan")
        for layer in data:
            data_index = data.index(layer)
            lines = layer.split('\n')
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if 'M106' in line:
                    parts = line.split()
                    new_parts = [parts[0], 'P%d' % target_fan]
                    for i in parts:
                        if i[0] == 'S':
                            new_parts.append(i)
                    new_lines.append(' '.join(new_parts))
                        
            data[data_index] = '\n'.join(new_lines)
            
        return data
        

