#include <stdio.h>
#include <string.h>

#define MAKE_MAX 20
#define MODEL_MAX 20
#define MAX_CARS 100

enum car_type {GAS, ELECTRIC};
struct car_t {
        char make[MAKE_MAX];
        char model[MODEL_MAX];
        enum car_type kind;
        union {
                // The following structs "overlap" (use the same memory)
                // so only one at a time can be used. The "kind" variable
                // above tells you which one is currently being used.
                struct {
                        unsigned int num_motors;
                        unsigned int kilowatts;
                        float mpkh;
                } electric;
                struct {
                        float liters;
                        float tanksize;
                        float mpg;
                } gas;
        } details;
};


int main(void)
{
        struct car_t cars[MAX_CARS];

        // Set the details for a gas vehicle
        strcpy(cars[0].make, "Dodge");
        strcpy(cars[0].model, "RAM");
        cars[0].kind = GAS;
        cars[0].details.gas.liters = 6.3;
        cars[0].details.gas.tanksize = 20;
        cars[0].details.gas.mpg = 12;

        // Set the details for an electric vehicle
        strcpy(cars[0].make, "Tesla");
        strcpy(cars[0].model, "Model S");
        cars[0].kind = ELECTRIC;
        cars[0].details.electric.num_motors= 2;
        cars[0].details.electric.kilowatts = 90;
        cars[0].details.electric.mpkh = 3;

        return(0);
}
