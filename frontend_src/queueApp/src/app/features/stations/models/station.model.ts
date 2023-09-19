export interface StationRaw {
  id: number;
  name: string;
  is_active: boolean;
}

export class Station {
  id: number;
  name: string;
  isActive: boolean;

  constructor(station: StationRaw) {
    this.id = station.id;
    this.name = station.name;
    this.isActive = station.is_active;
  }

  public toRaw(): StationRaw {
    return {
      id: this.id,
      name: this.name,
      is_active: this.isActive
    }
  }
}
