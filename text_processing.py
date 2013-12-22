import re
import base64
from PIL import Image
import cStringIO

canvasData = request.POST.get('imageData', '');