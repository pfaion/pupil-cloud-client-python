# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pupilcloud.configuration import Configuration


class RecordingWithFiles(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'account_id': 'str',
        'app_version': 'str',
        'created_at': 'datetime',
        'device_model': 'str',
        'device_name': 'str',
        'download_url': 'str',
        'duration': 'str',
        'duration_ns': 'int',
        'file_ids': 'list[str]',
        'files': 'list[RecordingFile]',
        'gaze_offset': 'OffsetCorrection',
        'glasses_id': 'str',
        'id': 'str',
        'is_uploaded': 'bool',
        'is_viewable': 'bool',
        'label_ids': 'list[str]',
        'name': 'str',
        'recorded_at': 'datetime',
        'sensors': 'list[str]',
        'size': 'int',
        'template_data': 'object',
        'template_id': 'str',
        'transcoded_url': 'str',
        'updated_at': 'datetime',
        'uploaded_bytes': 'int',
        'wearer_id': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'app_version': 'app_version',
        'created_at': 'created_at',
        'device_model': 'device_model',
        'device_name': 'device_name',
        'download_url': 'download_url',
        'duration': 'duration',
        'duration_ns': 'duration_ns',
        'file_ids': 'file_ids',
        'files': 'files',
        'gaze_offset': 'gaze_offset',
        'glasses_id': 'glasses_id',
        'id': 'id',
        'is_uploaded': 'is_uploaded',
        'is_viewable': 'is_viewable',
        'label_ids': 'label_ids',
        'name': 'name',
        'recorded_at': 'recorded_at',
        'sensors': 'sensors',
        'size': 'size',
        'template_data': 'template_data',
        'template_id': 'template_id',
        'transcoded_url': 'transcoded_url',
        'updated_at': 'updated_at',
        'uploaded_bytes': 'uploaded_bytes',
        'wearer_id': 'wearer_id'
    }

    def __init__(self, account_id=None, app_version=None, created_at=None, device_model=None, device_name=None, download_url=None, duration=None, duration_ns=None, file_ids=None, files=None, gaze_offset=None, glasses_id=None, id=None, is_uploaded=None, is_viewable=None, label_ids=None, name=None, recorded_at=None, sensors=None, size=None, template_data=None, template_id=None, transcoded_url=None, updated_at=None, uploaded_bytes=None, wearer_id=None, local_vars_configuration=None):  # noqa: E501
        """RecordingWithFiles - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._app_version = None
        self._created_at = None
        self._device_model = None
        self._device_name = None
        self._download_url = None
        self._duration = None
        self._duration_ns = None
        self._file_ids = None
        self._files = None
        self._gaze_offset = None
        self._glasses_id = None
        self._id = None
        self._is_uploaded = None
        self._is_viewable = None
        self._label_ids = None
        self._name = None
        self._recorded_at = None
        self._sensors = None
        self._size = None
        self._template_data = None
        self._template_id = None
        self._transcoded_url = None
        self._updated_at = None
        self._uploaded_bytes = None
        self._wearer_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if app_version is not None:
            self.app_version = app_version
        if created_at is not None:
            self.created_at = created_at
        if device_model is not None:
            self.device_model = device_model
        if device_name is not None:
            self.device_name = device_name
        if download_url is not None:
            self.download_url = download_url
        if duration is not None:
            self.duration = duration
        if duration_ns is not None:
            self.duration_ns = duration_ns
        if file_ids is not None:
            self.file_ids = file_ids
        if files is not None:
            self.files = files
        if gaze_offset is not None:
            self.gaze_offset = gaze_offset
        if glasses_id is not None:
            self.glasses_id = glasses_id
        if id is not None:
            self.id = id
        if is_uploaded is not None:
            self.is_uploaded = is_uploaded
        if is_viewable is not None:
            self.is_viewable = is_viewable
        if label_ids is not None:
            self.label_ids = label_ids
        if name is not None:
            self.name = name
        if recorded_at is not None:
            self.recorded_at = recorded_at
        if sensors is not None:
            self.sensors = sensors
        if size is not None:
            self.size = size
        if template_data is not None:
            self.template_data = template_data
        if template_id is not None:
            self.template_id = template_id
        if transcoded_url is not None:
            self.transcoded_url = transcoded_url
        if updated_at is not None:
            self.updated_at = updated_at
        if uploaded_bytes is not None:
            self.uploaded_bytes = uploaded_bytes
        if wearer_id is not None:
            self.wearer_id = wearer_id

    @property
    def account_id(self):
        """Gets the account_id of this RecordingWithFiles.  # noqa: E501


        :return: The account_id of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RecordingWithFiles.


        :param account_id: The account_id of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def app_version(self):
        """Gets the app_version of this RecordingWithFiles.  # noqa: E501


        :return: The app_version of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this RecordingWithFiles.


        :param app_version: The app_version of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._app_version = app_version

    @property
    def created_at(self):
        """Gets the created_at of this RecordingWithFiles.  # noqa: E501


        :return: The created_at of this RecordingWithFiles.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RecordingWithFiles.


        :param created_at: The created_at of this RecordingWithFiles.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def device_model(self):
        """Gets the device_model of this RecordingWithFiles.  # noqa: E501


        :return: The device_model of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this RecordingWithFiles.


        :param device_model: The device_model of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._device_model = device_model

    @property
    def device_name(self):
        """Gets the device_name of this RecordingWithFiles.  # noqa: E501


        :return: The device_name of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this RecordingWithFiles.


        :param device_name: The device_name of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def download_url(self):
        """Gets the download_url of this RecordingWithFiles.  # noqa: E501


        :return: The download_url of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this RecordingWithFiles.


        :param download_url: The download_url of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def duration(self):
        """Gets the duration of this RecordingWithFiles.  # noqa: E501


        :return: The duration of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RecordingWithFiles.


        :param duration: The duration of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def duration_ns(self):
        """Gets the duration_ns of this RecordingWithFiles.  # noqa: E501


        :return: The duration_ns of this RecordingWithFiles.  # noqa: E501
        :rtype: int
        """
        return self._duration_ns

    @duration_ns.setter
    def duration_ns(self, duration_ns):
        """Sets the duration_ns of this RecordingWithFiles.


        :param duration_ns: The duration_ns of this RecordingWithFiles.  # noqa: E501
        :type: int
        """

        self._duration_ns = duration_ns

    @property
    def file_ids(self):
        """Gets the file_ids of this RecordingWithFiles.  # noqa: E501


        :return: The file_ids of this RecordingWithFiles.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids):
        """Sets the file_ids of this RecordingWithFiles.


        :param file_ids: The file_ids of this RecordingWithFiles.  # noqa: E501
        :type: list[str]
        """

        self._file_ids = file_ids

    @property
    def files(self):
        """Gets the files of this RecordingWithFiles.  # noqa: E501


        :return: The files of this RecordingWithFiles.  # noqa: E501
        :rtype: list[RecordingFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this RecordingWithFiles.


        :param files: The files of this RecordingWithFiles.  # noqa: E501
        :type: list[RecordingFile]
        """

        self._files = files

    @property
    def gaze_offset(self):
        """Gets the gaze_offset of this RecordingWithFiles.  # noqa: E501


        :return: The gaze_offset of this RecordingWithFiles.  # noqa: E501
        :rtype: OffsetCorrection
        """
        return self._gaze_offset

    @gaze_offset.setter
    def gaze_offset(self, gaze_offset):
        """Sets the gaze_offset of this RecordingWithFiles.


        :param gaze_offset: The gaze_offset of this RecordingWithFiles.  # noqa: E501
        :type: OffsetCorrection
        """

        self._gaze_offset = gaze_offset

    @property
    def glasses_id(self):
        """Gets the glasses_id of this RecordingWithFiles.  # noqa: E501


        :return: The glasses_id of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._glasses_id

    @glasses_id.setter
    def glasses_id(self, glasses_id):
        """Sets the glasses_id of this RecordingWithFiles.


        :param glasses_id: The glasses_id of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._glasses_id = glasses_id

    @property
    def id(self):
        """Gets the id of this RecordingWithFiles.  # noqa: E501


        :return: The id of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecordingWithFiles.


        :param id: The id of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_uploaded(self):
        """Gets the is_uploaded of this RecordingWithFiles.  # noqa: E501


        :return: The is_uploaded of this RecordingWithFiles.  # noqa: E501
        :rtype: bool
        """
        return self._is_uploaded

    @is_uploaded.setter
    def is_uploaded(self, is_uploaded):
        """Sets the is_uploaded of this RecordingWithFiles.


        :param is_uploaded: The is_uploaded of this RecordingWithFiles.  # noqa: E501
        :type: bool
        """

        self._is_uploaded = is_uploaded

    @property
    def is_viewable(self):
        """Gets the is_viewable of this RecordingWithFiles.  # noqa: E501


        :return: The is_viewable of this RecordingWithFiles.  # noqa: E501
        :rtype: bool
        """
        return self._is_viewable

    @is_viewable.setter
    def is_viewable(self, is_viewable):
        """Sets the is_viewable of this RecordingWithFiles.


        :param is_viewable: The is_viewable of this RecordingWithFiles.  # noqa: E501
        :type: bool
        """

        self._is_viewable = is_viewable

    @property
    def label_ids(self):
        """Gets the label_ids of this RecordingWithFiles.  # noqa: E501


        :return: The label_ids of this RecordingWithFiles.  # noqa: E501
        :rtype: list[str]
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        """Sets the label_ids of this RecordingWithFiles.


        :param label_ids: The label_ids of this RecordingWithFiles.  # noqa: E501
        :type: list[str]
        """

        self._label_ids = label_ids

    @property
    def name(self):
        """Gets the name of this RecordingWithFiles.  # noqa: E501


        :return: The name of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecordingWithFiles.


        :param name: The name of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def recorded_at(self):
        """Gets the recorded_at of this RecordingWithFiles.  # noqa: E501


        :return: The recorded_at of this RecordingWithFiles.  # noqa: E501
        :rtype: datetime
        """
        return self._recorded_at

    @recorded_at.setter
    def recorded_at(self, recorded_at):
        """Sets the recorded_at of this RecordingWithFiles.


        :param recorded_at: The recorded_at of this RecordingWithFiles.  # noqa: E501
        :type: datetime
        """

        self._recorded_at = recorded_at

    @property
    def sensors(self):
        """Gets the sensors of this RecordingWithFiles.  # noqa: E501


        :return: The sensors of this RecordingWithFiles.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this RecordingWithFiles.


        :param sensors: The sensors of this RecordingWithFiles.  # noqa: E501
        :type: list[str]
        """

        self._sensors = sensors

    @property
    def size(self):
        """Gets the size of this RecordingWithFiles.  # noqa: E501


        :return: The size of this RecordingWithFiles.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RecordingWithFiles.


        :param size: The size of this RecordingWithFiles.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def template_data(self):
        """Gets the template_data of this RecordingWithFiles.  # noqa: E501


        :return: The template_data of this RecordingWithFiles.  # noqa: E501
        :rtype: object
        """
        return self._template_data

    @template_data.setter
    def template_data(self, template_data):
        """Sets the template_data of this RecordingWithFiles.


        :param template_data: The template_data of this RecordingWithFiles.  # noqa: E501
        :type: object
        """

        self._template_data = template_data

    @property
    def template_id(self):
        """Gets the template_id of this RecordingWithFiles.  # noqa: E501


        :return: The template_id of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this RecordingWithFiles.


        :param template_id: The template_id of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def transcoded_url(self):
        """Gets the transcoded_url of this RecordingWithFiles.  # noqa: E501


        :return: The transcoded_url of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._transcoded_url

    @transcoded_url.setter
    def transcoded_url(self, transcoded_url):
        """Sets the transcoded_url of this RecordingWithFiles.


        :param transcoded_url: The transcoded_url of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._transcoded_url = transcoded_url

    @property
    def updated_at(self):
        """Gets the updated_at of this RecordingWithFiles.  # noqa: E501


        :return: The updated_at of this RecordingWithFiles.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RecordingWithFiles.


        :param updated_at: The updated_at of this RecordingWithFiles.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def uploaded_bytes(self):
        """Gets the uploaded_bytes of this RecordingWithFiles.  # noqa: E501


        :return: The uploaded_bytes of this RecordingWithFiles.  # noqa: E501
        :rtype: int
        """
        return self._uploaded_bytes

    @uploaded_bytes.setter
    def uploaded_bytes(self, uploaded_bytes):
        """Sets the uploaded_bytes of this RecordingWithFiles.


        :param uploaded_bytes: The uploaded_bytes of this RecordingWithFiles.  # noqa: E501
        :type: int
        """

        self._uploaded_bytes = uploaded_bytes

    @property
    def wearer_id(self):
        """Gets the wearer_id of this RecordingWithFiles.  # noqa: E501


        :return: The wearer_id of this RecordingWithFiles.  # noqa: E501
        :rtype: str
        """
        return self._wearer_id

    @wearer_id.setter
    def wearer_id(self, wearer_id):
        """Sets the wearer_id of this RecordingWithFiles.


        :param wearer_id: The wearer_id of this RecordingWithFiles.  # noqa: E501
        :type: str
        """

        self._wearer_id = wearer_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecordingWithFiles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordingWithFiles):
            return True

        return self.to_dict() != other.to_dict()