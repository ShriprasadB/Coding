/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const combine = arr1.concat(arr2);
    const merged = {};

    combine.forEach((obj) => {
        const id = obj.id;
        if (!merged[id]){
            merged[id] = { ...obj };
        }
        else{
            merged[id] = { ...merged[id], ...obj };
        }
    });

    const joined = Object.values(merged);
    joined.sort((a,b) => a.id - b.id);

    return joined;
};