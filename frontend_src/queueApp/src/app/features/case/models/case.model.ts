export interface CaseRaw {
  id: number;
  name: string;
  description: string;
  symbol: string;
}


export class Case {
  id: number;
  name: string;
  description: string;
  symbol: string;

  constructor(data: CaseRaw) {
    this.id = data.id;
    this.name = data.name;
    this.description = data.description;
    this.symbol = data.symbol;
  }

  public static toRaw(caseObj: Case): CaseRaw {
    return {
      id: caseObj.id,
      name: caseObj.name,
      description: caseObj.description,
      symbol: caseObj.symbol,
    };
  }
}
