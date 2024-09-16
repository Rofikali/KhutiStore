import os
import random
from django.core.management.base import BaseCommand

# from your_app.models import Post  # Import your Post model
# PostsModel
from khutiwebsite.postsapi.models import PostsModel
from django.contrib.auth.models import User  # Import User model
from faker import Faker
from django.utils.text import slugify
from django.core.files.base import ContentFile
from PIL import Image
import io


class Command(BaseCommand):
    help = "Populate the Post model with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()  # Fetch all available users

        if not users.exists():
            self.stdout.write(
                self.style.ERROR(
                    "No users found! Please create users before running this command."
                )
            )
            return

        for _ in range(1000):
            # Generate fake data for each field
            title = fake.sentence(nb_words=6)
            description = fake.paragraph(nb_sentences=5)
            slug = slugify(title)
            image = self.generate_image()
            author = random.choice(users)  # Randomly pick an author

            # Create a new Post object
            post = PostsModel.objects.create(
                title=title,
                description=description,
                slug=slug,
                author=author,
            )

            # Save the image file
            post.image.save(
                f"image_{post.id}.png", ContentFile(image.getvalue()), save=True
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully added 1000 fake posts with images")
        )

    def generate_image(self):
        # Create an image using Pillow (100x100 with random colors)
        image = Image.new(
            "RGB",
            (100, 100),
            color=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        )

        # Save the image to a BytesIO object
        image_io = io.BytesIO()
        image.save(image_io, format="PNG")
        image_io.seek(0)

        return image_io
