import {bootstrapApplication} from "@angular/platform-browser";
import {AppComponent} from "./app/app.component";
import {provideRouter} from "@angular/router";
import {ROUTES} from "./app/routes";
import {enableProdMode, importProvidersFrom} from "@angular/core";
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {TokenInterceptor} from "./app/features/auth/interceptors/http-token-interceptor";
import {MatSnackBarModule} from "@angular/material/snack-bar";


bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(ROUTES),
    importProvidersFrom(HttpClientModule),
    importProvidersFrom(MatSnackBarModule),
    importProvidersFrom(BrowserAnimationsModule),
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true,
    },
  ]
}).catch((err) => {
  console.error(err)
});
