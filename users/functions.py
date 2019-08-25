


def get_current_role(request):
	current_role = "member"
	if request.user.is_authenticated:
		if request.user.is_superuser:
			current_role = "superadmin"
	return current_role
