from fastapi import HTTPException, status


class BuildsSystemException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(
            self,
            status_code: status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail: str = ""
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class BuildFileNotExists(BuildsSystemException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Build file not exists: "

    def __init__(
            self,
            file_path: str
    ) -> None:
        super().__init__(self.status_code, self.detail + file_path)


class IncorrectBuildFileException(BuildsSystemException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Build is incorrect: "

    def __init__(
            self,
            details: str
    ) -> None:
        super().__init__(self.status_code, self.detail + details)


class TasksKeyError(BuildsSystemException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Tasks does not contains: "

    def __init__(self, task_name: str) -> None:
        super().__init__(self.status_code, self.detail + task_name)
