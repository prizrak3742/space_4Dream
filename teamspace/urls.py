from django.urls import path


from .views import (
    AllMembersView, CreateTeamView, ListTeamView,
    EditMembersView, DeleteMembersView, EditTeamView, DeleteTeamView,
    CreateProjectView, MemberProjectView, ListProjectView,
    UpdateProjectView, DeleteProjectView, TaskProjectView,
    CreateTaskView, CompleteTaskView, UpdateTaskStatusView,
    UpdateTaskView, DeleteTaskView, DocHubView,
    AddDocHubView, UpdateDocHubView, DeleteDocHubView
)

app_name = "teamspace"

urlpatterns = [
    path("all_members/", AllMembersView.as_view(), name="all_members"),
    path("edit_menu/<int:pk>/", EditMembersView.as_view(), name="edit_member"),
    path("delete_menu/<int:pk>/", DeleteMembersView.as_view(), name="delete_member"),

    path("teams/", ListTeamView.as_view(), name="teams_list"),
    path("create_team/", CreateTeamView.as_view(), name="create_team"),
    path("update_team/<int:pk>/", EditTeamView.as_view(), name="edit_team"),
    path("delete_team/<int:pk>/", DeleteTeamView.as_view(), name="delete_team"),

    path("projects/", ListProjectView.as_view(), name="project_list"),
    path("create_project/", CreateProjectView.as_view(), name="create_project"),
    path("update_project/<int:pk>/", UpdateProjectView.as_view(), name="update_project"),
    path("delete_project/<int:pk>/", DeleteProjectView.as_view(), name="delete_project"),

    path("member_project/<int:pk>/", MemberProjectView.as_view(), name="member_project"),

    path("task_project/<int:pk>/", TaskProjectView.as_view(), name="task_project"),
    path("create_task/<int:pk>/", CreateTaskView.as_view(), name="create_task"),
    path("update_task/<int:pk>/", UpdateTaskView.as_view(), name="update_task"),
    path("delete_task/<int:pk>/", DeleteTaskView.as_view(), name="delete_task"),
    path("complete_task/<int:pk>/", CompleteTaskView.as_view(), name="complete_task"),
    path("status_task/<int:pk>/", UpdateTaskStatusView.as_view(), name="status_task"),

    path("dochub/<int:pk>/", DocHubView.as_view(), name="dochub"),
    path("load_document/<int:pk>/", AddDocHubView.as_view(), name="load_document"),
    path("update_document/<int:pk>/", UpdateDocHubView.as_view(), name="update_document"),
    path("delete_document/<int:pk>/", DeleteDocHubView.as_view(), name="delete_document"),
]
