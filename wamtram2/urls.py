from django.urls import path
from . import views

app_name = "wamtram2"


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("turtles/", views.TurtleListView.as_view(), name="turtle_list"),
    path("turtles/<int:pk>/", views.TurtleDetailView.as_view(), name="turtle_detail"),
    path("new-data-entry/<int:batch_id>/", views.TrtDataEntryFormView.as_view(), name="newtrtdataentry"),
    path("new-data-entry/<int:batch_id>/<int:turtle_id>/", views.TrtDataEntryFormView.as_view(), name="existingtrtdataentry"),
    path("data-entry/<int:entry_id>/", views.TrtDataEntryFormView.as_view(), name="trtdataentry"),
    path("find-tagged-turtle/<int:batch_id>/", views.FindTurtleView.as_view(), name="find_turtle"),
    # path("entry-batches/", views.EntryBatchesListView.as_view(), name="entry_batches"),
    path("entry-batches/<int:batch_id>/", views.EntryBatchDetailView.as_view(), name="entry_batch_detail"),
    path("delete-entry/<int:pk>/<int:batch_id>/", views.DeleteEntryView.as_view(), name="delete_entry"),
    path("new-entry-batch/", views.EntryBatchDetailView.as_view(), name="new_batch_detail"),
    path("delete-batch/<int:batch_id>/", views.DeleteBatchView.as_view(), name="delete_batch"),
    path("validate-data-entry-batch/<int:batch_id>/", views.ValidateDataEntryBatchView.as_view(), name="validate_data_entry_batch"),
    path("process-data-entry-batch/<int:batch_id>/", views.ProcessDataEntryBatchView.as_view(), name="process_data_entry_batch"),
    path("observations/<int:pk>/", views.ObservationDetailView.as_view(), name="observationdetail"),
    path('validate-tag/', views.ValidateTagView.as_view(), name='validate_tag'),
    path("templates-manage/", views.TemplateManageView.as_view(), name="template_manage"),
    path("templates-manage/<str:template_key>/", views.TemplateManageView.as_view(), name="template_manage_key"),
    path('templates-manage/get-places/', views.TemplateManageView.as_view(), name='get_template_places'),
    path('search-persons/', views.search_persons, name='search-persons'),
    path('search-places/', views.search_places, name='search-places'),
    path('export/', views.ExportDataView.as_view(), name='export_data'),
    path('dud-tag-manage/', views.DudTagManageView.as_view(), name='dud_tag_manage'),
    path('batches-curation/', views.BatchesCurationView.as_view(), name='batches_curation'),
    path('create-new-entry/', views.CreateNewEntryView.as_view(), name='create_new_entry'),
    path('quick-add-batch/', views.quick_add_batch, name='quick_add_batch'),
    path('batch_code_manage/', views.BatchCodeManageView.as_view(), name='batch_code_manage'),
    path('batch_code_manage/<int:batch_id>/', views.BatchCodeManageView.as_view(), name='batch_detail_manage'),
    path('get-places/', views.get_places, name='get_places'),
    path('check_batch_code/', views.BatchCodeManageView.as_view(), name='check_batch_code'),
    path('get_place_full_name/', views.get_place_full_name, name='get_place_full_name'),
    path('check_template_name/', views.check_template_name, name='check_template_name'),
    path('search-templates/', views.search_templates, name='search_templates'),
    path('add_person/', views.AddPersonView.as_view(), name='add_person'),
    path('api/available-batches/', views.AvailableBatchesView.as_view(), name='available_batches'),
    path('api/batch/<int:batch_id>/info/', views.BatchInfoView.as_view(), name='batch_info'),
    path('api/move-entry/', views.MoveEntryView.as_view(), name='move_entry'),
    path('curation/persons/manage/', views.PersonManageView.as_view(), name='manage_person'),
    path('curation/tags-register/', views.TagRegisterView.as_view(), name='tag_register'),
    path('turtle/<int:pk>/export/', views.TurtleDetailView.as_view(http_method_names=['get']), name='export_turtle_word'),
    path('admin-tools/', views.AdminToolsView.as_view(), name='admin_tools'),
    path('curation/pit-tags/', views.PitTagsListView.as_view(), name='pit_tags_list'),
    path('curation/flipper-tags/', views.FlipperTagsListView.as_view(), name='flipper_tags_list'),
    path('curation/transfer-observations-by-tag/', views.TransferObservationsByTagView.as_view(), name='transfer_observations_by_tag'),
    path('curation/nesting-seasons/', views.NestingSeasonListView.as_view(), name='nesting_season_list'),
    path('curation/batches/', views.BatchCurationView.as_view(), name='batch_curation'),
    path('curation/batch/<int:batch_id>/entries/', views.EntryCurationView.as_view(), name='entries_curation'),
    path('curation/batch/multi-entries/', views.EntryCurationView.as_view(), name='multi_entries_curation'),
    path('save-entry-changes/', views.SaveEntryChangesView.as_view(), name='save_entry_changes'),
    path('api/observations/<int:observation_id>/', views.ObservationDataView.as_view(), name='observation_detail'),
    path('curation/turtle-management/', views.TurtleManagementView.as_view(), name='turtle_management'),
    path('curation/observations-management/<int:observation_id>/',views.ObservationManagementView.as_view(), name='observation_management'),
    path('api/turtle-search/', views.TurtleManagementView.as_view(), name='turtle_search'),
    path('api/turtle-update/', views.TurtleManagementView.as_view(), name='turtle_update'),
    path('api/observations/<int:observation_id>/save/', views.SaveObservationView.as_view(), name='save_observation'),
    path('api/observations/save/', views.SaveObservationView.as_view(), name='create_observation'),
    path('api/flipper-tags-update/', views.FlipperTagsUpdateView.as_view(), name='flipper_tags_update'),
    path('api/pit-tags-update/', views.PitTagsUpdateView.as_view(), name='pit_tags_update'),
    path('api/identifications-update/', views.IdentificationsUpdateView.as_view(), name='identifications_update'),
    path('api/samples-update/', views.SamplesUpdateView.as_view(), name='samples_update'),
    path('api/documents-update/', views.DocumentsUpdateView.as_view(), name='documents_update'),
    path('api/recorded-tags/update/', views.RecordedTagsUpdateView.as_view(), name='recorded_tags_update'),
    path('api/recorded-pit-tags/update/', views.RecordedPitTagsUpdateView.as_view(), name='recorded_pit_tags_update'),
    path('api/recorded-identifications/update/', views.RecordedIdentificationsUpdateView.as_view(), name='recorded_identifications_update'),
    path('api/recorded-measurements/update/', views.RecordedMeasurementsUpdateView.as_view(), name='recorded_measurements_update'),
    path('api/recorded-damage/update/', views.RecordedDamageUpdateView.as_view(), name='recorded_damage_update'),
    path('api/recorded-scars/update/', views.RecordedScarsUpdateView.as_view(), name='recorded_scars_update'),
    path('curation/nesting-season-stats/', views.NestingSeasonStatsView.as_view(), name='nesting_season_stats'),
    path('batch-create-batches/', views.BatchCreateBatchesView.as_view(), name='batch_create_batches'),
    path('batches-review/', views.BatchesReviewView.as_view(), name='batches_review'),
]
