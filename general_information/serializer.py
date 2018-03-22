from rest_framework import serializers

from general_information.models import GeneralInformation, Publication, Contributor, Documentation


class GeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = ("home_title",
                  "home_information",
                  "home_video_file",
                  "docs_title",
                  "docs_information",
                  "about_GTE_title",
                  "about_GTE_information",
                  "about_contributors_title",
                  "about_publications_title",
                )

    def to_representation(self, instance):

        serialized_data = super(GeneralInformationSerializer, self).to_representation(instance)
        publications = Publication.objects.filter(general_information_publication_id=instance.id)
        serialized_data["about_publications_information"] = []
        for publication in publications:

            publication_obj = {}
            publication_obj["text"] = publication.text
            publication_obj["title"] = publication.title
            serialized_data["about_publications_information"].append(publication_obj)

        contributors = Contributor.objects.filter(general_information_contributor_id=instance.id)
        serialized_data["about_contributors_information"] = []
        for contributor in contributors:
            contributor_obj = {}
            contributor_obj["text"] = contributor.text
            serialized_data["about_contributors_information"].append(contributor_obj)

        jsonDocs = Documentation.objects.get()
        serialized_data["docs_menu"] = jsonDocs.docs_json.url

        return serialized_data
