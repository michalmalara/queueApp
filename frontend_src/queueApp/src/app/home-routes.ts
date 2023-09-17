import {Route} from "@angular/router";

export const HOME_ROUTES: Route[] = [
  {
    path: 'choose-station',
    loadComponent: () => import('./views/choose-station-view/choose-station-view.component').then(mod => mod.ChooseStationViewComponent)
  },
]
