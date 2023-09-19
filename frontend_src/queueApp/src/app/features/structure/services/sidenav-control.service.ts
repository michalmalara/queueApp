import {Injectable} from '@angular/core';
import {BehaviorSubject} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class SidenavControlService {
  private sidenavOpen$ = new BehaviorSubject<boolean>(false)

  constructor() {
  }

  public toggleSidenav() {
    this.sidenavOpen$.next(!this.sidenavOpen$.value)
  }

  public isSidenavOpen() {
    return this.sidenavOpen$.asObservable()
  }
}
