from fields import DicomField
from pydicom.dataelem import DataElement

# مثال عنصر DICOM
element = DataElement(0x00100010, 'PN', 'John Doe')  # PatientName
field = DicomField(element, element.keyword, str(element.tag))

# أظهر البصمة
print("Modified by:", field.modified_by)
