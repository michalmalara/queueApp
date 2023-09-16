import {Route} from "@angular/router";

export const ROUTES: Route[] = [
  {path: 'kiosk', loadComponent: () => import('./views/kiosk/kiosk.component').then(mod => mod.KioskComponent)},
];

