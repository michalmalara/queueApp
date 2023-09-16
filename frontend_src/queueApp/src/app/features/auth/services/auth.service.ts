import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable, of} from "rxjs";
import {catchError, map, tap} from "rxjs/operators";
import {Router} from "@angular/router";
import * as wasi from "wasi";

interface TokenResponse {
  access: string;
  refresh: string;
}

@Injectable({
  providedIn: "root",
})
export class AuthService {
  private readonly JWT_TOKEN = "JWT_TOKEN";
  private readonly REFRESH_TOKEN = "REFRESH_TOKEN";
  private loggedUser: string | null = "";

  constructor(
    private httpClient: HttpClient,
    private router: Router,
  ) {
  }

  login(username: string, password: string): Observable<boolean> {
    return this.httpClient.post<any>(`api/token/`, {username, password}).pipe(
      tap((tokens) => this.doLoginUser(username, tokens)),
      map((res) => {
        return res;
      }),
      catchError((error) => {
        alert(error.error);
        return of(false);
      })
    );
  }

  logout() {
    this.loggedUser = null;
    this.doLogoutUser();
  }

  isLoggedIn() {
    return !!this.getJwtToken();
  }

  refreshToken() {
    return this.httpClient
      .post<TokenResponse>(`api/token/refresh/`, {
        refresh: this.getRefreshToken(),
      })
      .pipe(
        tap((tokens) => {
          this.storeTokens(tokens);
        }),
        catchError((error) => {
          this.doLogoutUser();
          return of(false);
        })
      );
  }

  getJwtToken() {
    return localStorage.getItem(this.JWT_TOKEN);
  }

  private doLoginUser(username: string, tokens: TokenResponse) {
    this.loggedUser = username;
    this.storeTokens(tokens);
  }

  private doLogoutUser() {
    this.loggedUser = null;
    this.removeTokens();
    this.router.navigate(["/"]);
  }

  private getRefreshToken() {
    return localStorage.getItem(this.REFRESH_TOKEN);
  }

  private storeTokens(tokens: TokenResponse) {
    localStorage.setItem(this.JWT_TOKEN, tokens.access);
    localStorage.setItem(this.REFRESH_TOKEN, tokens.refresh);
  }

  private removeTokens() {
    localStorage.removeItem(this.JWT_TOKEN);
    localStorage.removeItem(this.REFRESH_TOKEN);
  }

}
