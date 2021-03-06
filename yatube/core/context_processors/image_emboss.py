from PIL import ImageFilter, Image


def emboss(request):   # noqa
    #     """
    #     # Create a new image with the given size
    #     def create_image(i, j):
    #         image = Image.new("RGB", (i, j), "white")
    #         return image

    #     # Get the pixel from the given image
    #     def get_pixel(image, i, j):   # noqa
    #         # Inside image bounds?
    #         width, height = image.size
    #         if i > width or j > height:
    #             return None

    #         # Get Pixel
    #         pixel = image.getpixel((i, j))
    #         return pixel

    #     # Limit maximum value to 255
    #     def get_max(value):    # noqa
    #         if value > 255:
    #             return 255

    #         return int(value)

    #     # Sepia is a filter based on exagerating red, yellow and brown tones
    #     # This implementation exagerates mainly yellow with a little brown
    #     def get_sepia_pixel(red, green, blue, alpha):   # noqa
    #         # This is a really popular implementation
    #         tRed = get_max((0.759 * red) + (0.398 * green) + (0.194 * blue))
    #         tGreen = (get_max((0.676 * red) + (0.354 * green)
    #                   + (0.173 * blue)))
    #         tBlue = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))

    #         # Return sepia color
    #         return tRed, tGreen, tBlue, alpha

    #     # Convert an image to sepia
    #     def convert_sepia(image):   # noqa
    #         # Get size
    #         width, height = image.size

    #         # Create new Image and a Pixel Map
    #         new = create_image(width, height)
    #         pixels = new.load()

    #         # Convert each pixel to sepia
    #         for i in range(0, width, 1):
    #             for j in range(0, height, 1):
    #                 p = get_pixel(image, i, j)
    #                 pixels[i, j] = get_sepia_pixel(p[0], p[1], p[2], 255)

    #         # Return new image
    #         return new

    #     # Return the color average
    #     def color_average(image, i0, j0, i1, j1):   # noqa
    #         # Colors
    #         red, green, blue, alpha = 0, 0, 0, 255

    #         # Get size
    #         width, height = image.size

    #         # Check size restrictions for width
    #         i_start, i_end = i0, i1
    #         if i0 < 0:
    #             i_start = 0
    #         if i1 > width:
    #             i_end = width

    #         # Check size restrictions for height
    #         j_start, j_end = j0, j1
    #         if j0 < 0:
    #             j_start = 0
    #         if j1 > height:
    #             j_end = height

    #         # This is a lazy approach,
    #         # we discard half the pixels we are comparing
    #         # This will not affect the end result, but increase speed
    #         count = 0
    #         for i in range(i_start, i_end - 2, 2):
    #             for j in range(j_start, j_end - 2, 2):
    #                 count += 1
    #                 p = get_pixel(image, i, j)
    #                 red, green, blue = p[0] + redImage, ImageDraw,
    #             red /= count
    #             green /= count
    #             blue /= count
    #         except Exception:
    #             pass

    #         # Return color average
    #         return int(red), int(green), int(blue), alpha

    #     # Create a Pointilize version of the image
    #     def convert_pointilize(image):    # noqa
    #         # Get size
    #         width, height = image.size

    #         # Radius
    #         radius = 3

    #         # Intentional error on the positionning
    #         # of dots to create a wave-like effect
    #         count = 0
    #         errors = [1, 0, 1, 1, 2, 3, 3, 1, 2, 1]

    #         # # Create new Image
    #         # new = create_image(width, height)

    #         # The ImageDraw module provide simple 2D graphics
    #         # for Image objects
    #         draw = ImageDraw.Draw(image)

    #         # Draw circles
    #         for i in range(0, width, radius + 3):
    #             for j in range(0, height, radius + 3):
    #                 # Get the color average
    #                 color = color_average(image, i - radius, j - radius,
    #                                       i + radius, j + radius)

    #                 # Set error in positions for I and J
    #                 eI = errors[count % len(errors)]
    #                 count += 1
    #                 eJ = errors[count % len(errors)]

    #                 # Create circle
    #                 draw.ellipse((i - radius + eI, j - radius + eJ,
    #                               i + radius + eI, j + radius + eJ),
    #                               fill=(color))

    #         # Return new image
    #         return image

    #     imj_obj = convert_pointilize(convert_sepia(
    #         Image.open("static/img//about/brat.png")))
    # """
    imj_obj = Image.open("static/img/about/zenit_lev_en.png")
    # imj_obj.filter(ImageFilter.GaussianBlur(radius=1.63)).show()
    # (ImageEnhance.Brightness(
    #     ImageOps.grayscale(imj_obj)
    #     .filter(ImageFilter.GaussianBlur(radius=2.3))
    #     .filter(ImageFilter.EMBOSS)).enhance(2)
    #     .filter(ImageFilter.SMOOTH()).show())
    return {'emboss': imj_obj.filter(ImageFilter.EMBOSS)}
