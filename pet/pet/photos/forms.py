from django import forms

from core.form_mixins import DisableFormMixin
from pet.common.models import PhotoLike, PhotoComment
import cloudinary.uploader
import cloudinary
from pet.photos.models import Photo


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')

        labels = {
            'photo': 'upload image',
            'description': 'description',
            'location': 'location',
            'tagged_pets': 'tag pets',
        }


class PhotoCreateForm(BasePhotoForm):
    pass


class PhotoEditForm(BasePhotoForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo', 'user')


class PhotoDeleteForm(DisableFormMixin, BasePhotoForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo', 'user')

    disabled_fields = ('description', 'location', 'tagged_pets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()          # add disabled fields

    def save(self, commit=True):        # overwrite save() method when delete photo

        if commit:
            self.instance.tagged_pets.clear()       # clear all tagged pets many-to-many connection

            # clear all tagged pates from the photo one-to-many connection
            Photo.objects.all().first().tagged_pets.clear()

            # clear all likes from the photo one-to-many connection
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()

            # clear all comments from the photo one-to-many connection
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()

            self.instance.delete()                  # delete the photo

        cloudinary.uploader.destroy(self.instance.photo.public_id, invalidate=True)
        return self.instance
