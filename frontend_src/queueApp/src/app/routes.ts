import {Route} from "@angular/router";

export const ROUTES: Route[] = [
  {path: '/', loadComponent: () => import('./app.component').then(mod => mod.AppComponent)},
];
