clc;clear all;close all;

tic
m       = 0.1;
Fricc   = 0.1;
long    = 0.6;
g       = 9.8;
M       = 0.5;
h       = 0.0001;
tiempo  = 1.5/h;
p_pp    = 0;
tita_pp = 0;
omega(1)= 0;

%Condiciones iniciales
alfa(1) = -0.01;
p(1)    = 0;
p_p(1)  = 0;
u(1)    = 0;
p(1)    = 0;
i       = 1;

%Versión linealizada en el equilibrio estable. Sontag Pp 104.
%estado=[p(i); p_p(i); alfa(i); omega(i)]
Mat_A   = [0 1 0 0;...
          0 -Fricc/M -m*g/M 0;...
          0 0 0 1;...
          0 Fricc/(long*M) g*(m+M)/(long*M) 0];
Mat_B   = [0;...
           1/M;...
           0;...
           -1/(long*M)];
X0      = [0 0 0 0]';
x       = [0 0 alfa(1) 0]';

while(i<(tiempo+1))

    %Variables del sistema no lineal
    estado  = [p(i); p_p(i); alfa(i); omega(i)];
    u(i)    = 0;
    
    %Sistema no lineal
    p_pp        = (1/(M+m)) * (u(i) - m*long*tita_pp*cos(alfa(i)) + m*long*omega(i)^2*sin(alfa(i)) - Fricc*p_p(i));
    tita_pp     = (1/long) * (g*sin(alfa(i)) - p_pp*cos(alfa(i)));
    
    p_p(i+1)    = p_p(i) + h*p_pp;
    p(i+1)      = p(i) + h*p_p(i);
    omega(i+1)  = omega(i) + h*tita_pp;
    alfa(i+1)   = alfa(i) + h*omega(i);
    
    %Variables del sistema lineal
    pl(i) = x(1); p_pl(i) = x(2); alfal(i) = x(3); omegal(i) = x(4);
    
    %Sistema lineal
    xp  = Mat_A*(x-X0) + Mat_B*u(i);
    x   = x + h*xp;
    i   = i+1;
end

TCalculo = toc

t         = 0:i-1;
t         = t*h;
u(i)      = 0;
pl(i)     = x(1);
p_pl(i)   = x(2);
alfal(i)  = x(3);
omegal(i) = x(4);

hfig1 = figure(1);
set(hfig1, 'Visible', 'off');
hold on;
title('Velocidad angular \omega [rad/s]',"fontsize",12);
xlabel('Tiempo [s]',"fontsize",10);
ylabel('\omega',"rotation",0);
plot(t,omega,'--b',"displayname","Exacta");
plot(t,omegal,':r',"displayname","Lineal");
legend("location","bestoutside");
grid on;
print('figura1','-landscape','-r500',"-dpng")

hfig2 = figure(2);
set(hfig1, 'Visible', 'off');
hold on;
title('Angulo \alpha [rad]',"fontsize",12);
xlabel('Tiempo [s]',"fontsize",10);
ylabel('\alpha',"rotation",0);
plot(t, alfa,'--b',"displayname","Exacta");
plot(t, -pi*ones(size(t)),'r',"displayname","Posición Neutra");
plot(t, alfal,':r',"displayname","Lineal");
legend("location","bestoutside");
grid on;
print('figura2','-landscape','-r500',"-dpng")

hfig3 = figure(3);
set(hfig1, 'Visible', 'off');
hold on;
title('Posicion carro [m]',"fontsize",12);
xlabel('Tiempo [s]',"fontsize",10);
ylabel('\delta',"rotation",0);
plot(t,p,'--b',"displayname","Exacta");
plot(t,pl,':r',"displayname","Lineal");
legend("location","bestoutside");
grid on;
print('figura3','-landscape','-r500',"-dpng")

hfig4 = figure(4);
set(hfig1, 'Visible', 'off');
hold on;
title('Velocidad carro [m/s]',"fontsize",12);
xlabel('Tiempo [s]',"fontsize",10);
ylabel('V [m/s]',"rotation",0);
plot(t,p_p,'--b',"displayname","Exacta");
plot(t,p_pl,':r',"displayname","Lineal");
legend("location","bestoutside");
grid on;
print('figura4','-landscape','-r500',"-dpng")

hfig5 = figure(5);
set(hfig1, 'Visible', 'off');
hold on;
title('Accion de control');
xlabel('Tiempo en Seg.');
plot(t,u,'b');
grid on;
print('figura5','-landscape','-r500',"-dpng")

hfig6 = figure(6);
set(hfig1, 'Visible', 'off');
hold on;
xlabel('Angulo \phi [rad]',"fontsize",10);
ylabel('Velocidad angular \omega [rad/s]',"fontsize",10);
plot(alfa,omega,'--b',"displayname","Exacta");
plot(alfal,omegal,':r',"displayname","Lineal");
legend("location","bestoutside");
grid on;
print('figura6','-landscape','-r500',"-dpng")

hfig7 = figure(7);
set(hfig1, 'Visible', 'off');
hold on;
plot(p,p_p,'--b',"displayname","Exacta");
plot(pl,p_pl,':r',"displayname","Lineal");
xlabel('Posicion carro \delta [m]',"fontsize",10);
ylabel('Velocidad carro v [m/s]',"fontsize",10);
legend("location","bestoutside");
grid on;
print('figura7','-landscape','-r500',"-dpng");

close all;
%figure(1);

%figure(2);

%figure(3);
%print('figura3','-landscape','-r500',"-dpng")
%figure(4);
%print('figura4','-landscape','-r500',"-dpng")
%figure(5);
%print('figura5','-landscape','-r500',"-dpng")
%figure(6);
%print('figura6','-landscape','-r500',"-dpng")
%figure(7);
%print('figura7','-landscape','-r500',"-dpng")
%print(hfig1,'VE_temporal','-dpng');
%print(hfig2,'VE_fases','-dpng');
%save('Datos_Controlador.mat','-v7');