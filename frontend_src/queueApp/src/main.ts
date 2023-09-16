import {bootstrapApplication} from "@angular/platform-browser";
import {AppComponent} from "./app/app.component";
import {provideRouter} from "@angular/router";
import {ROUTES} from "./app/routes";
import {APP_BASE_HREF} from "@angular/common";


bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(ROUTES),
  ]
});
