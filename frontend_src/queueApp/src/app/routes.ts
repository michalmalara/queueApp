import {Route} from "@angular/router";

export const ROUTES: Route[] = [
  {path: 'kiosk', loadComponent: () => import('./views/kiosk/kiosk.component').then(mod => mod.KioskComponent)},
  {
    path: 'login',
    loadComponent: () => import('./views/login-view/login-view.component').then(mod => mod.LoginViewComponent)
  },
  // {path: '**', loadComponent: () => import('./views/not-found/not-found.component').then(mod => mod.NotFoundComponent)}
];

