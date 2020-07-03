export const updateObject = (oldObject , updateProperties) => {
    return {
        ...oldObject, //spread 
        ...updateProperties
    }
}