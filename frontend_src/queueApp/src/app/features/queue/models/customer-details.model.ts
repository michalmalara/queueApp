export interface CustomerDetailsModelRaw {
  id: number,
  case: number,
  case_symbol: string,
  number: number,
  datetime_created: Date,
  datetime_started: Date | null,
  datetime_completed: Date | null,
  is_completed: boolean,
  station: number | null,
  other_queues: number,
}

export class CustomerDetails {
  id: number
  case: number
  caseSymbol: string
  number: number
  datetimeCreated: Date
  datetimeStarted: Date | null
  datetimeCompleted: Date | null
  isCompleted: boolean
  station: number | null
  otherQueues: number

  constructor(raw: CustomerDetailsModelRaw) {
    this.id = raw.id
    this.case = raw.case
    this.caseSymbol = raw.case_symbol
    this.number = raw.number
    this.datetimeCreated = new Date(raw.datetime_created)
    this.datetimeStarted = raw.datetime_started ? new Date(raw.datetime_started) : null
    this.datetimeCompleted = raw.datetime_completed ? new Date(raw.datetime_completed) : null
    this.isCompleted = raw.is_completed
    this.station = raw.station
    this.otherQueues = raw.other_queues
  }

  public static toRaw(customerDetails: CustomerDetails): CustomerDetailsModelRaw {
    return {
      id: customerDetails.id,
      case: customerDetails.case,
      case_symbol: customerDetails.caseSymbol,
      number: customerDetails.number,
      datetime_created: customerDetails.datetimeCreated,
      datetime_started: customerDetails.datetimeStarted,
      datetime_completed: customerDetails.datetimeCompleted,
      is_completed: customerDetails.isCompleted,
      station: customerDetails.station,
      other_queues: customerDetails.otherQueues,
    }
  }
}
