function bisectionMethod(func, xl, xu, es, maxit) {
    let iter = 0;
    let xr = 0;
    let ea = 0;
    let fl = func(xl);

    while (iter < maxit) {
        xr = (xl + xu) / 2;
        let fr = func(xr);

        if (fr === 0.0) {
            break;
        } else if (fl * fr < 0) {
            xu = xr;
        } else {
            xl = xr;
            fl = fr;
        }

        ea = (xu - xl) / xu * 100.0;
        if (ea < es) {
            break;
        }

        iter++;
    }

    return xr;
}

// Example usage
let func = x => x ** 2 - 4;
let xl = 1;
let xu = 4;
let es = 0.5;
let maxit = 50;
let result = bisectionMethod(func, xl, xu, es, maxit);
console.log(result);
