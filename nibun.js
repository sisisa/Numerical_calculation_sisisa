// 関数f(x)
const f = function(x){
  return x*x*x-3*x*x+9*x-8;
};

// 二分法
const bisectionMethod = function(a, b, eps){
    const i = 0;
    const s = 0;
    while(!Math.abs(b - a) < eps){
        i++;
        s = (a+b)/2.0
        if(f(s) * f(a)<0) b = s;
        else a = s;
        if(i==1000) break; // 1000回繰り返したら強制終了

    }  
    return s;
    
};


window.onload=function () {
    alert(bisectionMethod(0.0, 4.0, 0.0001)); // 1.1659055841222132
};