from vector import Vector2


class Force:

    def __init__(self, name):
        self.name = name


    def calculate(self, body_a, body_b=None):
        """
        محاسبه نیرو بین اجسام
        نسخه پایه فعلاً نیروی صفر برمی‌گرداند
        """

        return Vector2(0, 0)


    def apply(self, body, force_vector):
        """
        اعمال نیرو به جسم
        """

        body.apply_force(force_vector)


    def __str__(self):

        return f"Force: {self.name}"