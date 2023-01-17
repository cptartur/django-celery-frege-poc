import pytest

from fregepoc.analyzers.core import AnalyzerFactory
from fregepoc.analyzers.tests.swift.constants import MOCKED_SWIFT_FILES
from fregepoc.repositories.constants import ProgrammingLanguages
from fregepoc.repositories.factories import RepositoryFileFactory


@pytest.mark.django_db
class TestSwiftAnalyzerParameterCount:
    @pytest.mark.parametrize(
        ["repo_file_params", "expected_average_parameter_count"],
        [
            (
                {"repo_relative_file_path": "binary_search.swift"},
                3.0,
            ),
            (
                {"repo_relative_file_path": "bucket_sort.swift"},
                1.3,
            ),
            (
                {"repo_relative_file_path": "dijkstra.swift"},
                1.4,
            ),
        ],
    )
    def test_count_loc(
        self, repo_file_params, expected_average_parameter_count, settings, dummy_repo
    ):
        settings.DOWNLOAD_PATH = MOCKED_SWIFT_FILES
        analyzers = AnalyzerFactory.make_analyzers(ProgrammingLanguages.SWIFT)
        repo_file = RepositoryFileFactory(
            repository=dummy_repo,
            language=ProgrammingLanguages.SWIFT,
            **repo_file_params,
        )
        for analyzer in analyzers:
            actual = analyzer.analyze(repo_file)
            assert actual["average_parameter_count"] == pytest.approx(
                expected_average_parameter_count, 0.01
            )