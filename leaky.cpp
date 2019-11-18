#include<unistd.h>
//#include<dos.h>
#include<iostream>
#include<stdlib.h>
//#include<time.h>

#define bucketSize 512
using namespace std;
void bktInput(int a,int b);
int main(){
int op,packet_size;
cout<<"Enter the output rate: ";
cin>>op;
for(int i=1;i<=3;i++){
usleep(rand()%1000);
packet_size = rand()%1000;
cout<<"\nPacket No.: "<<i<<"\t";
cout<<"Packet size: "<<packet_size;
bktInput(packet_size,op);
}return 0;
}
void bktInput(int a,int b){
if(a>bucketSize){
cout<<"Bucket Overflow !!";
}
else{
usleep(500);
while(a>b){
cout<<b<<"bytes outputted"<<endl;
a-=b;
usleep(500);
}
}
if(a>0){
cout<<"Bucket Output: "<<a<<"bytes";
cout<<"Bucket outputted successfully";
}
}
/*
Enter the output rate: 100

Packet No.: 1	Packet size: 886Bucket Overflow !!Bucket Output: 886bytesBucket outputted successfully
Packet No.: 2	Packet size: 915Bucket Overflow !!Bucket Output: 915bytesBucket outputted successfully
Packet No.: 3	Packet size: 335100bytes outputted
100bytes outputted
100bytes outputted
*/
