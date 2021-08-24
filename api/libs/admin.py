# django imports
from django.contrib import admin


class AbstractBaseModelAdmin(admin.ModelAdmin):
    """
    Abstract base class based on ModelAdmin
    """

    ordering = ('-id',)
    show_full_result_count = False

    def get_actions(self, request):
        """
        This removes the option to delete selected instances
        """
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False
