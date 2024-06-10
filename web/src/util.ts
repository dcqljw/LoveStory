export const setCookie = (key:any, value:any) => {
    const date = new Date();
    date.setTime(date.getTime() + (7 * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${key}=${value};${expires}`
}
export const getCookie = (key:any) => {
    let cookie_str = document.cookie;
    let cookie_list = cookie_str.split(";");
    for (const cookie of cookie_list) {
        let cookie_k_v = cookie.split("=");
        if (key === cookie_k_v[0]) {
            return cookie_k_v[1]
        }
    }
    return null
}