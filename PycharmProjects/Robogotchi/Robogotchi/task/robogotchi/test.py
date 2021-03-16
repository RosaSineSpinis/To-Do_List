class Test:
    def __init__(self):
        self.overheat = 30
        self.overheat_previous = 10
        self.robot_name = "Daneel"

        output = f"{self.robot_name}'s level of overheat was "+ \
                      f"{self.overheat_previous}. Now it is {self.overheat}.\n\n"+\
                 f"{self.robot_name} cooled off!"
        print(output)
        print("fun", self.sleep_what_prints(output))

    def sleep_what_prints(self, output):
        if self.overheat == 0 and self.overheat_previous == 0:
            if "Daneel is cool" not in output:
                return False
        else:
            if self.overheat != 0:
                insertion = '\nDaneel cooled off'
            else:
                insertion = '\nDaneel is cool'
            text = f"Daneel's level of overheat was {self.overheat_previous}. Now it is {self.overheat}.\n" \
                   f"{insertion}"
            print(text)
            text = text.split('\n')
            for tex in text:
                if tex.lower() not in output.lower():
                    return False
        return True


Test()