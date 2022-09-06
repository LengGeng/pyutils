from unittest import TestCase

from utils import ImageUtils


class TestImageUtils(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # test read_image
        cls.image = ImageUtils.read_image("images/template.jpg")

    def test_show_image(self):
        image = ImageUtils.read_image("images/targets.jpg")
        # show
        ImageUtils.show(image)
        # show_adapt
        ImageUtils.show_adapt(image)

    def test_save_image(self):
        ImageUtils.save_image(self.image, "images/template_copy.jpg")

    def test_image_convert_bytes(self):
        # ImageToBytes
        image_bytes = ImageUtils.cv2bytes(self.image)
        print(image_bytes)
        # BytesToImage
        convert_image = ImageUtils.bytes2cv(image_bytes)
        ImageUtils.save_image(convert_image, "images/template_bytes.jpg")

    def test_image_convert_base64(self):
        # ImageToBase64
        image_base64 = ImageUtils.image_to_base64(self.image)
        print(image_base64)
        # Base64ToImage
        convert_image = ImageUtils.base64_to_image(image_base64)
        ImageUtils.save_image(convert_image, "images/template_base_64.jpg")

    def test_image_size(self):
        self.assertEqual(ImageUtils.image_size(self.image), (122, 42))

    def test_check_gary(self):
        image_gary = ImageUtils.read_image("images/template_gary.jpg")
        self.assertTrue(ImageUtils.check_gray(image_gary))
        self.assertFalse(ImageUtils.check_gray(self.image))
