import {Route} from "@angular/router";
import {CanOpenGuard} from "./features/auth/guards/can-open.guard";

export const ROUTES: Route[] = [
  {
    path: '',
    loadComponent: () => import('./views/home-view/home-view.component').then(mod => mod.HomeViewComponent),
    loadChildren: () => import('./home-routes').then(mod => mod.HOME_ROUTES),
    canActivate: [CanOpenGuard]
  },
  {
    path: 'kiosk',
    loadComponent: () => import('./views/kiosk-view/kiosk-view.component').then(mod => mod.KioskViewComponent)
  },
  {
    path: 'login',
    loadComponent: () => import('./views/login-view/login-view.component').then(mod => mod.LoginViewComponent)
  },
  {
    path: 'queue/:queueId',
    loadComponent: () => import('./views/queue-details-view/queue-details-view.component').then(mod => mod.QueueDetailsViewComponent)
  },
  {
    path: '**',
    loadComponent: () => import('./views/not-found-view/not-found-view.component').then(mod => mod.NotFoundViewComponent)
  }
];
