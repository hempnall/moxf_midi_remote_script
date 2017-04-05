from moxf import moxf

def create_instance(c_instance):
    return moxf(c_instance)



from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=1891, product_ids=[408], model_name='MOXF'),
     PORTS_KEY: [inport(props=[NOTES_CC]), outport(props=[SCRIPT])]}
