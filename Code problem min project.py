class Image:
    def __init__(self, width=640, height=480, channels=3,
                 in_value=None):  # in_value defines value at which all values in image set to
        self.width = width
        self.height = height
        self.channels = channels
        self.pix = self._initialize_pix(in_value)

    # to create required dataset for storing value related to image
    def _initialize_pix(self, in_value):
        if in_value is None:
            in_value = 0
        if self.channels == 1:
            return [[in_value] * self.width for _ in range(self.height)]
        elif self.channels == 3:
            return [[(in_value,) * 3 for _ in range(self.width)] for _ in range(self.height)]

    # constructor for b/w and colour image
    @classmethod
    def create_bw_image(cls, width=640, height=480, in_value=1):
        return cls(width=width, height=height, channels=1, in_value=in_value)

    @classmethod
    def create_color_image(cls, width=640, height=480, in_value=(1, 1, 1)):
        return cls(width=width, height=height, channels=3, in_value=in_value)

    # for giving coordinates of pixel and intensity or rgb code
    def set_pixel(self, x, y, value):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError("Coordinates out of bounds.")

        if self.channels == 1:
            self.pix[y][x] = value
        elif self.channels == 3:
            self.pix[y][x] = value

    # to get value related to desired image
    def get_pixel(self, x, y):
        return self.pix[y][x]

    # to copy image
    def copy(self):
        new_image = Image(width=self.width, height=self.height, channels=self.channels)
        new_image.pix = [row.copy() for row in self.pix]
        return new_image


bw_image = Image.create_bw_image(height=22, width=25, in_value=1)
bw_image.set_pixel(10, 20, 150)
color_image = Image.create_color_image(width=800, height=600, in_value=(255, 255, 255))
copied = bw_image.copy()

print(bw_image.get_pixel(10, 20))
print(bw_image.width)
