from django.contrib import admin

from.import models

class DepartmentAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 5
    list_dispay=('department_name',)
admin.site.register(models.Department,DepartmentAdmin)

class HODAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 5
    list_dispay=('HOD_name','email','age','date_registered','branches','department')
admin.site.register(models.HOD,HODAdmin)

class sponserAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 5
    list_dispay=('full_name','email','sponsernumber','age','Region','image','date_registered','department')
admin.site.register(models.sponser,sponserAdmin)

class staffAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 5
    list_dispay=('staff_name','email','image','date_registered','branches','department')
admin.site.register(models.staff,staffAdmin)

class AnnouncementsAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 5
    list_dispay=('heading','title','date_registered',' file')
admin.site.register(models.Announcements,AnnouncementsAdmin)

class branchesAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 5
    list_dispay=('branch_name',)
admin.site.register(models.branches,branchesAdmin)

class customerAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 5
    list_dispay=('full_name','email','purpose_of_loan','amount',' Loan_typelist','age','Region','image','date_registered','department')
    search_fields = ('full_name','email','purpose_of_loan','amount',' Loan_typelist','age','Region','image','date_registered','department')
admin.site.register(models.customer,customerAdmin)


class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'loan_amount', 'loan_period_months', 'total_payment', 'daily_payment', 'weekly_payment', 'monthly_payment')
    readonly_fields = ('total_payment', 'daily_payment', 'weekly_payment', 'monthly_payment')
admin.site.register(models.LoanApplication,LoanApplicationAdmin)


