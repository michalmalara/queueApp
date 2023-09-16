import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class RestClientService {
  private _basicRoute = 'api/'

  constructor(private httpClient: HttpClient) {
  }

  public get(url: string): Observable<any> {
    this._addBasicRoute(url);
    return this.httpClient.get(url);
  }

  public post(url: string, body: any): Observable<any> {
    this._addBasicRoute(url);
    return this.httpClient.post(url, body);
  }

  private _addBasicRoute(url: string): string {
    if (!url.startsWith('api/')) {
      url = this._basicRoute + url;
    }
    return url;
  }
}
