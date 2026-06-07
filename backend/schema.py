from enum import Enum

class Gender(str, Enum):
    Male = "Male"
    Female = "Female"


class YesNo(str, Enum):
    Yes = "Yes"
    No = "No"


class MultipleLinesType(str, Enum):
    Yes = "Yes"
    No = "No"
    NoPhoneService = "No phone service"


class InternetServiceType(str, Enum):
    DSL = "DSL"
    FiberOptic = "Fiber optic"
    No = "No"


class OnlineSecurityType(str, Enum):
    Yes = "Yes"
    No = "No"
    NoInternetService = "No internet service"


class ContractType(str, Enum):
    MonthToMonth = "Month-to-month"
    OneYear = "One year"
    TwoYear = "Two year"


class PaymentMethodType(str, Enum):
    ElectronicCheck = "Electronic check"
    MailedCheck = "Mailed check"
    BankTransfer = "Bank transfer (automatic)"
    CreditCard = "Credit card (automatic)"

from pydantic import BaseModel

class CustomerRequest(BaseModel):

    customerID: str

    gender: Gender

    SeniorCitizen: int

    Partner: YesNo
    Dependents: YesNo

    tenure: int

    PhoneService: YesNo
    MultipleLines: MultipleLinesType

    InternetService: InternetServiceType

    OnlineSecurity: OnlineSecurityType
    OnlineBackup: OnlineSecurityType
    DeviceProtection: OnlineSecurityType
    TechSupport: OnlineSecurityType

    StreamingTV: OnlineSecurityType
    StreamingMovies: OnlineSecurityType

    Contract: ContractType

    PaperlessBilling: YesNo

    PaymentMethod: PaymentMethodType

    MonthlyCharges: float
    TotalCharges: float