from django.contrib import admin
from .models import Student, Course, Grade
from django.db.models import Avg, Count
from django.utils.html import format_html
from django import forms

# Register your models here.
admin.site.site_header = "B-1140"


# admin.site.site_title = "3ri Technologies Pvt. Ltd."


class GradeInline(admin.StackedInline):
    model = Grade
    max_num = 3
    can_delete = False
    verbose_name_plural = "Grade"
    classes = ('collapse',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'percentage')
    list_display_links = ('first_name', 'last_name', 'percentage')
    list_filter = ('first_name',)

    # it works when we use to add the data.
    fields = ('first_name', 'last_name', 'courses')

    # def percentage(self, obj):
    #     return f"{obj.first_name} -- {obj.last_name}"

    def percentage(self, obj):
        result = list(Grade.objects.filter(student=obj).values('grade'))
        # result = Grade.objects.filter(student=obj).values_list('grade')
        stud_per = 0
        if result:
            stud_per = result[0]['grade']

        color = "blue"
        if stud_per > 80:
            color = "green"
        elif (stud_per < 80) and (stud_per > 50):
            color = "yellow"
        elif stud_per < 50:
            color = "red"
        return format_html("<span style='color:{}'>{}</span>", color, stud_per)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    list_display_links = ('name', 'year')
    list_filter = ('name', 'year')

    # inline
    inlines = (GradeInline,)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade')
    list_display_links = ('student', 'course', 'grade')
    list_filter = ('student', 'course', 'grade')


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)

# admin.site.site_header = "Custom Student Admin Project"
# admin.site.site_title = "Django Admin"
#
#
# class StudentAdminForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = "__all__"
#
#     def clean_first_name(self):
#         if self.cleaned_data["first_name"] == 'robot':
#             raise forms.ValidationError("Human Only")
#         return self.cleaned_data["first_name"]
#
#     def clean_last_name(self):
#         if len(self.cleaned_data["last_name"]) < 4:
#             raise forms.ValidationError("Length should be greater than 4")
#         return self.cleaned_data["last_name"]
#
#
# class GradeInline(admin.StackedInline):
#     model = Grade
#     max_num = 2
#     can_delete = False
#     verbose_name_plural = "Sample Title"
#     classes = ('collapse',)
#
#
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'year')
#     list_display_links = ('name', 'year')
#     # Add dynamic field that show number of students for a course
#
#     # make fields read only
#     # readonly_fields = ('name', )
#
#     # inlines
#     inlines = (GradeInline,)
#
#     list_filter = ('name', 'year')
#
#
# class GradeAdmin(admin.ModelAdmin):
#     list_display = ('student', 'course', 'grade')
#     list_display_links = ('student', 'course', 'grade')
#
#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name')
#     # list_display = ('first_name', 'last_name', 'percentage')
#     list_display_links = ('first_name', 'last_name')
#     fields = ('first_name', 'last_name', 'courses')
#     list_filter = ('first_name',)
#     form = StudentAdminForm
#
#     # def percentage(self, obj):
#     #     result = Grade.objects.filter(student=obj).aggregate(Avg('grade'))
#     #     avg = int(result["grade__avg"])
#     #     color = "blue"
#     #     if avg > 80:
#     #         color = "green"
#     #     elif (avg < 80) and (avg > 50):
#     #         color = "yellow"
#     #     elif avg < 50:
#     #         color = "red"
#     #
#     #     return format_html("<span style='color:{}'>{}</span>", color, avg)
#     #     # return result["grade__avg"]
#
#     def get_form(self, request, obj, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.base_fields["first_name"].label = "First Name(Only)"
#         return form


# admin.site.register(Course, CourseAdmin)
# admin.site.register(Grade, GradeAdmin)
# admin.site.register(Student, StudentAdmin)
