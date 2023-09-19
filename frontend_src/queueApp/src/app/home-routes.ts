import {Route} from "@angular/router";

export const HOME_ROUTES: Route[] = [
  {
    path: '',
    loadComponent: () => import('./views/station-view/station-view.component').then(mod => mod.StationViewComponent)
  }
]
