clc;clear all;

X       = [0; 0; 0; 100];
t_etapa = 10e-3;
tF      = 20;
color_  = 'r';
color   = 'b';
Ts      = t_etapa;
%t_u     = 0:0.1:2*pi;
%u       = sin(t_u);
ii      = 0;

for t=0:t_etapa:tF
  ii      = ii+1;
  x2(ii)  = X(2);
  x4(ii)  = X(4);
%  if t < tF/4
%    X     = modavion(t_etapa, X, sin(t/pi));
%    acc(ii) = sin(t/pi);
%    c1    = acc(end);
%  elseif (t >= tF/4) && (t < 3/4*tF)
%    X     = modavion(t_etapa, X, c1 - (0.05*t)**2);
%    acc(ii) = c1 - (0.05*t)**2;
%    c2    = acc(end);
%  else
%    X     = modavion(t_etapa, X, c2 + 0.02*t + sin(t/pi) );
%    acc(ii) = c2 + 0.02*t + sin(t/pi);
%  endif
  X       = modavion(t_etapa, X, 0.5*sin(pi*t));
  acc(ii) = 0.5*sin(pi*t);
end

t = 0:t_etapa:tF;

figura1 = figure(1);
subplot(3,1,1); hold on;

plot(t,x2,color_,"linewidth",2);
title('x_2 | angulo fi [rad]',"fontsize",12);
ylabel('\Phi',"fontsize",10,"rotation",0);
set(gca,"fontsize",8);
grid on;
hold on;

subplot(3,1,2);hold on;
plot(t,x4,color_,"linewidth",2);
title('x_4 | Altura [m]',"fontsize",12);
ylabel('h',"fontsize",10,"rotation",0);
set(gca,"fontsize",8);
grid on;
hold on;

subplot(3,1,3);hold on;
plot(t,acc,color,"linewidth",2);
title('Entrada | u_t [rad], v_a',"fontsize",12);
ylabel('u',"fontsize",10,"rotation",0);
set(gca,"fontsize",8);
grid on;
hold on;

xlabel('Tiempo [Seg.]',"fontsize",10);
%saveas(figura1,"simulacion_1",'png');
print('simulacion_2','-landscape','-r400',"-dpng")