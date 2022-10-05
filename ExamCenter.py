class ExamCenter:
    def __init__(self, center_id, center_name, center_strength, center_status):
        self.center_id = center_id
        self.center_name = center_name
        self.center_strength = center_strength
        self.center_status = center_status

    def setCenterId(self, center_id):
        self.center_id = center_id

    def getCenterId(self):
        return self.center_id

    def setCenterStrength(self, center_strength):
        self.center_strength = center_strength

    def getCenterStrength(self):
        return self.center_strength

    def setCenterStatus(self, center_status):
        self.center_status = center_status

    def getCenterStatus(self):
        return self.center_status

    def setCenterId(self, center_name):
        self.center_name = center_name

    def getCenterName(self):
        return self.center_name

    def __str__(self) -> str:
        return super().__str__()
