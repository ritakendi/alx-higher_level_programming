exports.esrever = function (list) {
  const new_list = [];
  while (list.length){
    new_list.push(list.pop());
  }
  return new_list;
};
