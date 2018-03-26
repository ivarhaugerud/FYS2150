
data = load('terminal_hastighet.dat')
Fg = data(:, 1)
vel1 = data(:, 2)
vel2 = data(:, 3)
vel3 = data(:, 4)

[m, c, delta_c, delta_m] = function1(Fg, vel2.^2)
z = sqrt(m)
delta_z = z*0.5*delta_m/m
plot(Fg, vel2.^2)
hold on
plot(Fg, c + m*Fg)


%{
obj = imread('bilde5.png');
binary = im2bw(obj, 0.8);

a = size(binary);
i = 1:a(1);
e = ones(1, a(2));
b = i';
c = b*e;
size(I_y)
size(c)
I_y = c.*binary;
m = sum(sum(binary));
y_m = sum(I_y*e')/m

a = size(binary);
i = 1:a(2);
e = ones(1, a(1));
b = i';
c = b*e;
c_trans = c';
I_x = c_trans.*binary;
m = sum(sum(binary));
X_m = sum(e*I_x)/m
imshow(obj)
%}
%{
obj = imread('areal.png');
obj(:, 1:120, :) = 0;
obj(1:80, :, :) = 0;
obj(215:300, :, :) = 0;
obj(:, 550:692, :) = 0;
obj(:, :, 1) = 0;
obj(:, :, 2) = 0;
sum(sum(sum(obj)))/255
imshow(obj)
%}